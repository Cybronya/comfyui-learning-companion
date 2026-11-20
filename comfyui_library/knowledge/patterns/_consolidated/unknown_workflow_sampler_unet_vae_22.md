---
name: unknown_workflow_sampler_unet_vae_22
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.751208
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/1-Aiden-MiniMax_Music3测试工作流！！！_2088008118289653761.json, 音频生成/音频生成/A-18 MiniMax Music 3 文生音频 主题+歌词 歌曲直出_2107488878654480385.json, 音频生成/音频生成/MiniMax Music 3 - 音乐生成-支持提示词-歌词_2088208847331745794.json, 音频生成/音频生成/MiniMax Music 3 AI音乐歌曲创作工作流2608_2094013038423793665.json, 音频生成/音频生成/MiniMax Music 3 文生音频_2088066476321361922.json, 音频生成/音频生成/MiniMax Music 3 音乐生成_2091519854246457345.json, 音频生成/音频生成/MiniMax Music 3 音乐生成｜歌词结构标签+三段时间+120秒完整歌曲_2089294478686375938.json, 音频生成/音频生成/MiniMax Music 3歌曲创作_2096597355494731778.json, 音频生成/音频生成/MiniMax Music-音乐生成_2088831784896258049.json, 音频生成/音频生成/MiniMax Music3音乐生成_2088175617937334274.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089204171424755713.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089205528881876993.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089206267771449346.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089207088126976002.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089207882897256450.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089208516367175682.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089209296776159233.json, 音频生成/音频生成/MiniMax Music音乐生成_2088133517992620034.json, 音频生成/音频生成/MiniMax Music音乐生成_2088219988443357186.json, 音频生成/音频生成/MiniMax Music音乐生成_2088243433164075009.json, 音频生成/音频生成/MiniMax Music音乐生成_2088329185046654978.json, 音频生成/音频生成/MiniMax Music音乐生成_2088620802592825345.json, 音频生成/音频生成/MiniMax Music音乐生成_2089190873136459777.json, 音频生成/音频生成/MiniMax Music音乐生成_自动谱曲连接版_v4_2090433735576608769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（音频生成/音频生成/1-Aiden-MiniMax_Music3测试工作流！！！_2088008118289653761.json、音频生成/音频生成/A-18 MiniMax Music 3 文生音频 主题+歌词 歌曲直出_2107488878654480385.json、音频生成/音频生成/MiniMax Music 3 - 音乐生成-支持提示词-歌词_2088208847331745794.json、音频生成/音频生成/MiniMax Music 3 AI音乐歌曲创作工作流2608_2094013038423793665.json、音频生成/音频生成/MiniMax Music 3 文生音频_2088066476321361922.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 23/24 个有
- `VAEDecodeAudioTiled` —— 22/24 个有
- `ComfySwitchNode` —— 21/24 个有
- `SeedNode` —— 14/24 个有
- `PrimitiveStringMultiline` —— 10/24 个有
- `Float` —— 9/24 个有
- `CR Prompt Text` —— 8/24 个有
- `PrimitiveFloat` —— 8/24 个有
- `CR Text` —— 3/24 个有
- `PreviewAudio` —— 2/24 个有
- `JoinStrings` —— 1/24 个有
- `PreviewAny` —— 1/24 个有
- `RHLLMChatNode` —— 1/24 个有
- `RH_LLMAPI_Pro_Node` —— 1/24 个有
- `ShowText|pysssss` —— 1/24 个有
- `SomethingToString` —— 1/24 个有
- `孤海注释` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 40 | 24 | 93% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 24 | 100% |
| 采样算法 | euler | - | 24 | 96% |
| 调度器 | simple | - | 24 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 24/24 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 40，24 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 96%
- 调度器 最常用 simple，24 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：发现KSampler但没有VAEDecode
