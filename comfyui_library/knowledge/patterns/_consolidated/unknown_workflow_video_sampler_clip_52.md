---
name: unknown_workflow_video_sampler_clip_52
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.850727
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, ImageConcanate, ImageResizeKJ, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2双模型首尾帧图生视频_2080624345147334658.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2082282165500469249.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083014224594427906.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083105850020950017.json, 视频生成/图生视频/最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json, 视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json, 视频生成/图生视频/首尾震·2张照片丝滑变视频_2010988628385730561.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json, 视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json, 视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json, 视频生成/文生视频/动图首选+wan2.2首尾帧+全节点注释_2061457988065513474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan2.2双模型首尾帧图生视频_2080624345147334658.json、视频生成/图生视频/Wan2.2双模型首尾帧视频_2082282165500469249.json、视频生成/图生视频/Wan2.2双模型首尾帧视频_2083014224594427906.json、视频生成/图生视频/Wan2.2双模型首尾帧视频_2083105850020950017.json、视频生成/图生视频/最强首尾帧视频 - Wan2.2动漫模型DaSiWa-_2009700904043286530.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ImageConcanate`
- `ImageResizeKJ`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Images to RGB` —— 8/11 个有
- `Qwen3_VQA` —— 8/11 个有
- `easy textSwitch` —— 8/11 个有
- `intToFloat _O` —— 6/11 个有
- `GetNode` —— 4/11 个有
- `RH_LLMAPI_NODE` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `ImpactSwitch` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `Maoyu_ListToString` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有
- `YC_SingleTextNode` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 82% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 82%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
