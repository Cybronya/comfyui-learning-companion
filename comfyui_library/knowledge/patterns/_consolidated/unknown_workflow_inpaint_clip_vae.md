---
name: unknown_workflow_inpaint_clip_vae
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.899938
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/身材局部调节_1924737292291010562.json, 图片生成/图生图/身材局部调节用法补充_1963868766877863938.json, 平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json, 平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json, 平台全量/FLUX FILL去水印_1977345433607524354.json, 平台全量/FLUX FILL去除水印_1945130310420058114.json, 平台全量/FLUX FILL超强去水印工作流_1907097938781462529.json, 平台全量/FLUX Fill Outpaint_2070938167636742146.json, 平台全量/FLUX Fill Outpaint_2070984843839754242.json, 平台全量/FLUX.1 Fill 扩图 & 重绘 工作流_1863905133766836225.json, 平台全量/FLUX扩图工作流（大全）_1947133066378260481.json, 平台全量/FLUX扩图工作流（大全）_2018512176838873089.json, 平台全量/Flux Fill无痕扩图_1940418028628586498.json, 平台全量/OneReward扩图_1966333896126312450.json, 平台全量/inpainting&outpainting using flux fill fp8&GGUF_1863510757034930177.json, 平台全量/【阡陌】可输中文FLUX fill 无痕扩图工作流_1909451331734806529.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_vae

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/身材局部调节_1924737292291010562.json、图片生成/图生图/身材局部调节用法补充_1963868766877863938.json、平台全量/ComfyUI官方示例12：Flux.1 inpainting工作流 _ ComfyUI从入门到精通_1932782711759065090.json、平台全量/ComfyUI官方示例13：Flux.1 Outpainting工作流_ComfyUI从入门到精通_1932791703839330305.json、平台全量/FLUX FILL去水印_1977345433607524354.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 15/16 个有
- `UNETLoader` —— 14/16 个有
- `ImagePadForOutpaint` —— 10/16 个有
- `ConditioningZeroOut` —— 7/16 个有
- `Image Comparer (rgthree)` —— 5/16 个有
- `PreviewImage` —— 4/16 个有
- `UnetLoaderGGUF` —— 4/16 个有
- `LoraLoader` —— 3/16 个有
- `ImageConcanate` —— 2/16 个有
- `KSamplerAdvanced` —— 2/16 个有
- `DeepTranslatorTextNode` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 14 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 30 | 16 | 0% |
| 采样算法 | euler | - | 16 | 88% |
| 调度器 | normal | - | 16 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 30，16 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，16 个样本，一致性 88%
- 调度器 最常用 normal，16 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
