# Candi
An open-source API for accessing information about US political candidates.

## What is Candi?

Where do you find information about US election candidates?

Whatever your answer is, chances are it's less than ideal. Each state has an official register on their Secretary of State's website, but they're all obscured by their variable formatting, hidden behind dozens of useless links. External websites can share those same navigational difficulties, and, even worse, may be only sporadically updated and even run the risk of bias.

Overall, if the process of getting information about candidates is difficult for a normal voter, then it's near impossible for a developer working with this information at scale.

Candi aims to provide a common language for interacting with each state's official candidate registration records. Its open-source API gives developers access to a standardized, up-to-date database of political candidates that does not rely on external organizations, facilitating the rapid deployment of applications that keep America's democracy running.

## How do I use Candi?

Currently, Candi can be accessed via the [endpoint on my personal site](http://sam-holloway.com/candi/). Documentation on using the API is forthcoming, as I would prefer at least a few more states to be implemented before much usage occurs, but you can visit the [API Explorer](http://sam-holloway.com/candi/explorer/) to get a better idea of usage.

## How do I contribute to Candi?

Once again, it can be pretty hard to get information on candidates. Though Candi is being developed to combat this problem, it stands to reason that that development is no easy task. Candidates from each state must be found, parsed, and loaded into the Candi database differently. In order to accomplish our goal of providing as much standardized and up-to-date candidate information as possible, Candi needs contributions from developers willing to brave the remaining states' official candidate registers.

Please check the [State Status List](state_status_list.md) to see what's left to do and consult Candi's [Contribution Guidelines](contribution_guidelines.md) as you develop your contribution.