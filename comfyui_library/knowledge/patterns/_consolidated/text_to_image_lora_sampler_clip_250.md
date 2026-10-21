---
name: text_to_image_lora_sampler_clip_250
type: Text To Image
frequency: 5
level: strong
coverage: 0.8244
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptyMiniMaxMusic3LatentAudio, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxMusic3TextEncode, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/MiniMax_Music3音乐生成完结版｜歌曲信息歌词时长设置音频生成_2088724711751639042.json, 音频生成/音频生成/Minimax Music 3开源｜最长5分钟音乐生成音频生成_2089692123355500546.json, 音频生成/音频生成/Minimax Music3文生音频工作流｜音频生成_2090079394516791298.json, 音频生成/音频生成/Minimax Music3音乐生成神器开源版｜官方skill自动优化音频生成_2089728078477094913.json, 音频生成/音频生成/Music3音乐生成完结版｜MiniMax歌曲信息歌词一键成曲_2089067866262949890.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_250

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/MiniMax_Music3音乐生成完结版｜歌曲信息歌词时长设置音频生成_2088724711751639042.json、音频生成/音频生成/Minimax Music 3开源｜最长5分钟音乐生成音频生成_2089692123355500546.json、音频生成/音频生成/Minimax Music3文生音频工作流｜音频生成_2090079394516791298.json、音频生成/音频生成/Minimax Music3音乐生成神器开源版｜官方skill自动优化音频生成_2089728078477094913.json、音频生成/音频生成/Music3音乐生成完结版｜MiniMax歌曲信息歌词一键成曲_2089067866262949890.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyMiniMaxMusic3LatentAudio`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `SeedNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ImpactConditionalBranch` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VAEDecodeAudioTiled` —— 2/5 个有
- `ZML_BooleanSwitch` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `DapaoMusic3CaptionPromptNode` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
