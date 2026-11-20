---
name: unknown_workflow_sampler_clip_unet_109
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9202
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX Fill 手部修复工作流_2040689200806236162.json, 图片生成/图生图/FLUX Fill 扩图工作流_2091470617185964033.json, 图片生成/图生图/FLUX-Fill极致自动重绘修手_1920650639141961729.json, 图片生成/图生图/FLUX-无痕迹扩图无缝扩图强力版_1931324361393766402.json, 图片生成/图生图/FLUX_Fill_手部修复工作流_2096405989913350146.json, 图片生成/图生图/FLUX_Fill_手部修复工作流_2096417130290962433.json, 图片生成/图生图/FLUX无缝扩图_1900359454850953218.json, 图片生成/图生图/FULX无缝扩图（超好用）_1922928971468652546.json, 图片生成/图生图/最新Flux完美修手，支持各种风格图片手部修复v4_1938792048067858433.json, 图片生成/图生图/超高质量无缝扩图_1936427082933243906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX Fill 手部修复工作流_2040689200806236162.json、图片生成/图生图/FLUX Fill 扩图工作流_2091470617185964033.json、图片生成/图生图/FLUX-Fill极致自动重绘修手_1920650639141961729.json、图片生成/图生图/FLUX-无痕迹扩图无缝扩图强力版_1931324361393766402.json、图片生成/图生图/FLUX_Fill_手部修复工作流_2096405989913350146.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `ImagePadForOutpaint` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `ImageResize+` —— 4/10 个有
- `Int` —— 4/10 个有
- `LoraLoader` —— 4/10 个有
- `RepeatLatentBatch` —— 4/10 个有
- `easy hiresFix` —— 2/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `UltimateSDUpscale` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 15 - 28 | 10 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 1 | 0.85 - 1 | 4 | 93% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 15 - 28，10 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.85 - 1，4 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
