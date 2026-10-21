---
name: text_to_image_video_lora_sampler_54
type: Text To Image
frequency: 12
level: strong
coverage: 0.792083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json, 视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json, 视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json, 视频生成/图生视频/MinimaxH3视频生成工作台｜支持@图片直接驱动_2098702232026963970.json, 视频生成/图生视频/参考图生视频生成｜MiniMaxH3高质量出片工作流_2095049456667414529.json, 视频生成/文生视频/H3台词优化多合一极简版工作流 视频生成处理_2100665823122780162.json, 视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json, 视频生成/文生视频/MinimaxH3完美优化版 生视频质量与速度双优_2104296777661902850.json, 视频生成/文生视频/MinimaxH3完美优化版｜文生图生视频高质量生成_2094586726764343297.json, 视频生成/文生视频/MinimaxH3极简多合一优化版｜文生视频视频生视频全搞定_2089379554887553025.json, 视频生成/文生视频/MinimaxH3极简版多合一｜文生视频视频生视频_2095251267785420802.json, 视频生成/文生视频/极简版多合一0830｜MinimaxH3文生视频生视频_2095591499948978177.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json、视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json、视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json、视频生成/图生视频/MinimaxH3视频生成工作台｜支持@图片直接驱动_2098702232026963970.json、视频生成/图生视频/参考图生视频生成｜MiniMaxH3高质量出片工作流_2095049456667414529.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 9/12 个有
- `LoadVideo` —— 8/12 个有
- `LTXVSeparateAVLatent` —— 7/12 个有
- `LoadAudio` —— 7/12 个有
- `LoadImage` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `MinimaxH3LatentUpscaler3D` —— 7/12 个有
- `SetNode` —— 7/12 个有
- `SplitSigmas` —— 7/12 个有
- `GetNode` —— 6/12 个有
- `SaveImage` —— 6/12 个有
- `ModelAttentionBackend` —— 5/12 个有
- `ModelPreviewOverrideKJ` —— 5/12 个有
- `MiniMaxH3EasyMediaLoader` —— 3/12 个有
- `Fast Groups Muter (rgthree)` —— 2/12 个有
- `ImageResizeKJv2` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `RTXVideoSuperResolution` —— 2/12 个有
- `ResolutionSelector` —— 2/12 个有
- `TextInput_` —— 2/12 个有
- `VAEEncode` —— 2/12 个有
- `VAEEncodeAudio` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `workflow>声音` —— 2/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
