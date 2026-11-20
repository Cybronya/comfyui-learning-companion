---
name: unknown_workflow_video_sampler_clip_82
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.99575
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/53.tonnie-Smooth+FMLF 首尾多帧视频_2007957873501937666.json, 视频生成/图生视频/DaSiWaWan-V10-动漫首尾多帧视频生成_2043159910917087233.json, 视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json, 视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json, 视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json, 视频生成/图生视频/DasiwaWAN-V10-动漫图生视频+自动提示词_2043133353490128897.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034470406807101441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/53.tonnie-Smooth+FMLF 首尾多帧视频_2007957873501937666.json、视频生成/图生视频/DaSiWaWan-V10-动漫首尾多帧视频生成_2043159910917087233.json、视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json、视频生成/图生视频/DaSiWaWan2.2-动漫多帧视频生成_2007811222472761345.json、视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 7/8 个有
- `CLIPVisionEncode` —— 4/8 个有
- `CLIPVisionLoader` —— 4/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `ComfyMathExpression` —— 3/8 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `PainterI2V_Wan2_2` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `YC Color Match` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | beta | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 beta，8 个样本，一致性 75%
