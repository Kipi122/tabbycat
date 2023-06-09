<template>

  <td>
    <div class="ballot-cell pr-2">

      <div v-for="ballot in cellData.ballots" :key="ballot.id">

        <!-- If ballot was not entered by current user or user is admin -->
        <a :href="ballotLink(ballot)" v-if="canReviewBallot(ballot)" class="ballot-link">
          <del v-if="ballot.discarded">
            {{ ballotText(ballot) }} v{{ ballot.version }}
          </del>
          <span v-else>
            {{ ballotText(ballot) }} v{{ ballot.version }}
          </span>
        </a>

        <!-- If the ballot was entered by current user -->
        <span v-else class="ballot-link" data-toggle="tooltip"
              :title="gettext('You cannot confirm this ballot because you entered it')">
          <del v-if="ballot.discarded">
            {{ ballotText(ballot) }} v{{ ballot.version }}
          </del>
          <span v-else>
            {{ ballotText(ballot) }} v{{ ballot.version }}
          </span>
        </span>

        <!-- Ballot metadata -->
        <span class="small text-muted ballot-info">
          <span class="text-monospace">{{ ballot.short_time }} </span>
          <span class="text-info" v-if="ballot.private_url">{{ ballot.submitter }}</span>
          <span v-else>{{ ballot.submitter }}</span>
        </span>

      </div>

      <div v-if="canMergeCreate">
        <a :href="cellData.merge_ballot" v-text="gettext('Merge Ballot(s)')"></a>
      </div>

      <div v-if="needsNewBallot">
        <a :href="cellData.new_ballot" v-text="gettext('Add Ballot')"></a>
      </div>

    </div>
  </td>

</template>

<script>

export default {
  props: {
    cellData: Object,
  },
  computed: {
    viableBallotsCount: function () {
      return this.cellData.ballots.map((b) => {
        if (b.discarded) {
          return 1
        }
        return 0
      }).reduce((a, b) => a + b, 0)
    },
    needsNewBallot: function () {
      return this.viableBallotsCount === this.cellData.ballots.length
    },
    canMergeCreate: function () {
      // it's merge-able if there is at least one single-adj non-discarded ballot
      // (ok to have just one, since user might want to fill in the others)
      return this.cellData.ballots.some((b) => !b.discarded && b.single_adj)
    },
  },
  methods: {
    canReviewBallot: function (ballot) {
      if (this.cellData.acting_role === 'admin') {
        return true
      }
      if (this.cellData.current_user !== ballot.submitter) {
        return true
      }
      return false
    },
    ballotLink: function (ballot) {
      if (this.cellData.acting_role === 'admin') {
        return ballot.admin_link
      }
      return ballot.assistant_link
    },
    ballotText: function (ballot) {
      if (ballot.confirmed) {
        return this.gettext('Re-Edit')
      }
      return this.gettext('Review')
    },
  },
}

</script>
