---
name: unknown_workflow_video_sampler_clip_32
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.827923
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2007040869337145346.json, 视频生成/图生视频/1955097122862350338.json, 视频生成/图生视频/1966753554679705601.json, 视频生成/图生视频/2017158021029306369.json, 视频生成/图生视频/2044039756232790017.json, 视频生成/图生视频/1950018329094348802.json, 视频生成/图生视频/1961778127099904002.json, 视频生成/图生视频/1953457819821506562.json, 视频生成/图生视频/1954213178995568641.json, 视频生成/图生视频/1981037704194441217.json, 视频生成/图生视频/2053001977566638081.json, 视频生成/图生视频/2010988628385730561.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2007040869337145346.json、视频生成/图生视频/1955097122862350338.json、视频生成/图生视频/1966753554679705601.json、视频生成/图生视频/2017158021029306369.json、视频生成/图生视频/2044039756232790017.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/13 个有
- `LoraLoaderModelOnly` —— 10/13 个有
- `PathchSageAttentionKJ` —— 9/13 个有
- `CR Text` —— 8/13 个有
- `GetNode` —— 8/13 个有
- `ImpactSwitch` —— 8/13 个有
- `JWInteger` —— 8/13 个有
- `MathExpression|pysssss` —— 8/13 个有
- `RH_LLMAPI_NODE` —— 8/13 个有
- `SetNode` —— 8/13 个有
- `WanImageToVideo` —— 8/13 个有
- `easy showAnything` —— 8/13 个有
- `LayerUtility: PurgeVRAM V2` —— 6/13 个有
- `CLIPVisionEncode` —— 5/13 个有
- `CLIPVisionLoader` —— 5/13 个有
- `ImageConcanate` —— 5/13 个有
- `ImageResizeKJ` —— 5/13 个有
- `WanFirstLastFrameToVideo` —— 5/13 个有
- `ModelPatchTorchSettings` —— 4/13 个有
- `wanBlockSwap` —— 4/13 个有
- `SaveImage` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `RH_Nano_Banana_Image2Image` —— 1/13 个有
- `TT_img_enc` —— 1/13 个有
- `WanMotionScale` —— 1/13 个有
- `WanVideoNAG` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 54% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 13 | 83% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 77% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 54%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，13 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 77%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
