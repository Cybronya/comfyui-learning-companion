---
name: unknown_workflow_sampler_unet_vae_20
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.690118
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyMiniMaxMusic3LatentAudio, KSampler, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/MiniMax Music 3 文生音频官方流_2090455981170978818.json, 音频生成/音频生成/MiniMax Music 3 音乐生成_2091519854246457345.json, 音频生成/音频生成/MiniMax Music 3 音乐生成｜歌词结构标签+三段时间+120秒完整歌曲_2089294478686375938.json, 音频生成/音频生成/MiniMax Music 3歌曲创作_2096597355494731778.json, 音频生成/音频生成/MiniMax Music3 I 开源音乐新王_2088579603374895106.json, 音频生成/音频生成/MiniMax Music3音乐生成_2088175617937334274.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089204171424755713.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089205528881876993.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089206267771449346.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089207088126976002.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089207882897256450.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089208516367175682.json, 音频生成/音频生成/MiniMax Music3音乐生成_2089209296776159233.json, 音频生成/音频生成/MiniMax-Music3 官方skill自动提示词文生音乐流_2090618993068560385.json, 音频生成/音频生成/MiniMax_Music3-音乐生成_2090004883062747138.json, 音频生成/音频生成/Minimax Music 3音乐生成工作流_2088093007462617089.json, 音频生成/音频生成/MinimaxH3-music3_2094205332569550850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_20

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（音频生成/音频生成/MiniMax Music 3 文生音频官方流_2090455981170978818.json、音频生成/音频生成/MiniMax Music 3 音乐生成_2091519854246457345.json、音频生成/音频生成/MiniMax Music 3 音乐生成｜歌词结构标签+三段时间+120秒完整歌曲_2089294478686375938.json、音频生成/音频生成/MiniMax Music 3歌曲创作_2096597355494731778.json、音频生成/音频生成/MiniMax Music3 I 开源音乐新王_2088579603374895106.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyMiniMaxMusic3LatentAudio`
- `KSampler`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 16/17 个有
- `VAEDecodeAudioTiled` —— 16/17 个有
- `PrimitiveFloat` —— 14/17 个有
- `PrimitiveStringMultiline` —— 10/17 个有
- `SeedNode` —— 9/17 个有
- `Label (rgthree)` —— 2/17 个有
- `LoadImage` —— 2/17 个有
- `Text` —— 2/17 个有
- `DapaoLocalMusic3CaptionPromptNode` —— 1/17 个有
- `JjkText` —— 1/17 个有
- `String` —— 1/17 个有
- `easy showAnything` —— 1/17 个有
- `孤海注释` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 40 | 17 | 92% |
| Prompt 约束强度(CFG) | 1.7 | 1.7 - 1.7 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 17/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 40，17 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1.7，观测区间 1.7 - 1.7，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：发现KSampler但没有VAEDecode
