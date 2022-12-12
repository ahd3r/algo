const subs = {};

const publish = (event, payload) => {
  for (cb of subs[event]) {
    cb(payload)
  }
};

const subscribe = (event, cb) => {
  subs[event] = subs[event] ? [...subs[event], cb] : [cb];
  const unsubscribe = () => {
    subs[event] = subs[event].filter((subsCb)=>subsCb !== cb);
  };
  return unsubscribe
};
