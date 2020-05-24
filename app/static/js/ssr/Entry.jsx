import React from 'react';
import ReactMarkdown from 'react-markdown'

function Entry({ content }) {
  console.log(content);
  return (
    <div>
      <ReactMarkdown source={content} />
    </div>
  )
}

export default Entry;