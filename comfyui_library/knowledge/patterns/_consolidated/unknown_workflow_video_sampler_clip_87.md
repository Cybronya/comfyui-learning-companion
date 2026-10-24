---
name: unknown_workflow_video_sampler_clip_87
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.977286
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json, 视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json, 视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json, 视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json, 视频生成/图生视频/DasiwaWAN-V10-动漫图生视频+自动提示词_2043133353490128897.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034470406807101441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json、视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json、视频生成/图生视频/DaSiWaWan2.2-动漫图生视频_2007793632560025602.json、视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json、视频生成/图生视频/DasiwaWAN-V10-动漫图生视频+自动提示词_2043133353490128897.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `ModelPatchTorchSettings` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `CLIPVisionEncode` —— 5/7 个有
- `CLIPVisionLoader` —— 5/7 个有
- `WanFirstLastFrameToVideo` —— 5/7 个有
- `ComfyMathExpression` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PainterI2V_Wan2_2` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 7 | 89% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | beta | - | 7 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，7 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 beta，7 个样本，一致性 57%
