---
name: unknown_workflow_video_sampler_clip_110
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9735
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json, 视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json, 视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json, 视频生成/图生视频/DasiwaWAN-V10-动漫图生视频+自动提示词_2043133353490128897.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json, 视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034470406807101441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/251223001-14.WanSmoothMix首尾帧-NF_2003138334044168194.json、视频生成/图生视频/DaSiWaWan-V10-动漫首尾帧视频生成_2043155067376766978.json、视频生成/图生视频/DaSiWaWan2.2-动漫视首尾帧_2007802630776561666.json、视频生成/图生视频/DasiwaWAN-V10-动漫图生视频+自动提示词_2043133353490128897.json、视频生成/图生视频/Wan2.2-Remix-V3.0-首尾帧视频_2034096736225988609.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CLIPVisionEncode` —— 5/6 个有
- `CLIPVisionLoader` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `WanFirstLastFrameToVideo` —— 5/6 个有
- `ComfyMathExpression` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `PainterI2V_Wan2_2` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 83% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 6 | 88% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 50%
