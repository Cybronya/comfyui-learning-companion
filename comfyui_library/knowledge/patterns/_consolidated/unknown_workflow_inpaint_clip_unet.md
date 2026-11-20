---
name: unknown_workflow_inpaint_clip_unet
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.78375
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-fill 扩图工作流_1909483321586233345.json, 图片生成/图生图/Flux_Fill_Inpaint图像修复官方工作流_1930167104581046273.json, 图片生成/图生图/Flux_Fill_Outpaint图像扩展官方工作流_1930164307269468162.json, 图片生成/图生图/Flux完美扩图工作流_1918564228125360129.json, 图片生成/图生图/Flux局部内容重绘工作流生成或消除_1918553934582190081.json, 图片生成/图生图/Flux局部重绘工作流_1985263737491832833.json, 图片生成/图生图/Flux局部重绘工作流_1989256117442187265.json, 图片生成/图生图/Flux局部重绘工作流_2075150049822199809.json, 图片生成/图生图/Flux扩图工作流_1985266658258395138.json, 图片生成/图生图/Flux扩图工作流_1989256220538179585.json, 图片生成/图生图/OneReward扩图【基础流】_1966303400382164994.json, 图片生成/图生图/局部重绘与去水印_2106381323781894145.json, 图片生成/图生图/工作流基础篇-6-Flux局部重绘工作流_2016060930114723841.json, 图片生成/图生图/工作流基础篇-7-Flux扩图工作流_2016070044844822529.json, 平台全量/ComfyUI 扩图工作流_1969577869485744130.json, 平台全量/FLUX局部重绘_1980115726814056449.json, 平台全量/Flux完美消除水印工作流_1918518502905548802.json, 平台全量/Flux局部重绘 -去水印工作流（RunningHub）_1979087760223014914.json, 平台全量/Flux局部重绘工作流_1913045500935794689.json, 平台全量/Flux局部重绘工作流_1981286170397147138.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Flux-fill 扩图工作流_1909483321586233345.json、图片生成/图生图/Flux_Fill_Inpaint图像修复官方工作流_1930167104581046273.json、图片生成/图生图/Flux_Fill_Outpaint图像扩展官方工作流_1930164307269468162.json、图片生成/图生图/Flux完美扩图工作流_1918564228125360129.json、图片生成/图生图/Flux局部内容重绘工作流生成或消除_1918553934582190081.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 19/20 个有
- `Image Comparer (rgthree)` —— 17/20 个有
- `JWImageResizeByLongerSide` —— 16/20 个有
- `Anything Everywhere` —— 15/20 个有
- `PreviewImage` —— 12/20 个有
- `ImageToMask` —— 9/20 个有
- `ImagePadForOutpaint` —— 8/20 个有
- `MaskToImage` —— 8/20 个有
- `DeepTranslatorTextNode` —— 1/20 个有
- `ImageMaskSwitch` —— 1/20 个有
- `KSamplerAdvanced` —— 1/20 个有
- `RH_Translator` —— 1/20 个有
- `ShowText` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 19 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 30 | 20 | 0% |
| 采样算法 | dpmpp_2m | - | 20 | 80% |
| 调度器 | sgm_uniform | - | 20 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，19 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 30，20 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，20 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，20 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
