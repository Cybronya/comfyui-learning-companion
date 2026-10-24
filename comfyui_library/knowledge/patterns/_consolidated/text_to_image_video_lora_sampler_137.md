---
name: text_to_image_video_lora_sampler_137
type: Text To Image
frequency: 5
level: strong
coverage: 0.8174
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfySwitchNodeV2, EmptyLatentImage, FeiHouEasyH3RH, FeiHouEasyH3RHDurationCrop, FeiHouEasyH3RHLoraStack, FeiHouEasyH3RHOutput, FeiHouEasyH3RHPromptPreview, FeiHouEasyH3RHRemixLoader, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3SigmaShift, ModelAttentionBackend, RandomSeedNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax多参考生视频图生视频处理生成工具_2101773710939222018.json, 视频生成/图生视频/MiniMax多参考生视频图生视频处理生成工具_2102194422237720577.json, 视频生成/文生视频/H3 Remix极致简化无限画布式操作全功能提示词反推双采样_2100672031950983169.json, 视频生成/文生视频/极致简化MiniMax H3 Remix无限画布式操作加全功能提示词反推双采样_2108643289502142466.json, 视频生成/文生视频/极致简化MiniMax H3 Remix无限画布｜全功能提示词反推双采样_2108456403076734977.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax多参考生视频图生视频处理生成工具_2101773710939222018.json、视频生成/图生视频/MiniMax多参考生视频图生视频处理生成工具_2102194422237720577.json、视频生成/文生视频/H3 Remix极致简化无限画布式操作全功能提示词反推双采样_2100672031950983169.json、视频生成/文生视频/极致简化MiniMax H3 Remix无限画布式操作加全功能提示词反推双采样_2108643289502142466.json、视频生成/文生视频/极致简化MiniMax H3 Remix无限画布｜全功能提示词反推双采样_2108456403076734977.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNodeV2`
- `EmptyLatentImage`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHDurationCrop`
- `FeiHouEasyH3RHLoraStack`
- `FeiHouEasyH3RHOutput`
- `FeiHouEasyH3RHPromptPreview`
- `FeiHouEasyH3RHRemixLoader`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `RandomSeedNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `CFGGuider` —— 3/5 个有
- `EmptyMiniMaxH3LatentAV` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `FeiHouEasyH3RHFaceRefine` —— 3/5 个有
- `FeiHouEasyH3RHResolution` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImpactImageInfo` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `MiniMaxH3AddGuide` —— 3/5 个有
- `ModelPreviewOverrideKJ` —— 3/5 个有
- `RHSettingsNode` —— 3/5 个有

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
