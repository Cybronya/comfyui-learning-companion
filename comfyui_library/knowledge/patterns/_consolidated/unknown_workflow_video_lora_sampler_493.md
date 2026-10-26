---
name: unknown_workflow_video_lora_sampler_493
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9832
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json, 视频生成/图生视频/WH-AI-Studio-Wan2.2首帧-中间帧-尾帧（加速标准版首中尾帧图生视频）_2022240074083082242.json, 视频生成/图生视频/WH-AI-Studio（短剧必备）指定人物从指定场景出现（图生视频-加速完美版）（人物一致性）_2022215823229718529.json, 视频生成/图生视频/Wan2.2_14B_首尾帧生成视频极速版_1957122488750759938.json, 视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_493

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json、视频生成/图生视频/WH-AI-Studio-Wan2.2首帧-中间帧-尾帧（加速标准版首中尾帧图生视频）_2022240074083082242.json、视频生成/图生视频/WH-AI-Studio（短剧必备）指定人物从指定场景出现（图生视频-加速完美版）（人物一致性）_2022215823229718529.json、视频生成/图生视频/Wan2.2_14B_首尾帧生成视频极速版_1957122488750759938.json、视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `WanFirstLastFrameToVideo` —— 4/5 个有
- `ImageResizeKJ` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ImageColorMatch+` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageSmartSharpen+` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
