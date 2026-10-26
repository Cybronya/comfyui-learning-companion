---
name: unknown_workflow_sampler_clip_unet_203
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.826
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2文生图工作流--直出2K_1926661482686353410.json, 图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json, 图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json, 图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json, 图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json, 图片生成/文生图/反差人设-剧场后台花絮_1999861137980223490.json, "视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_203

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux2文生图工作流--直出2K_1926661482686353410.json、图片生成/文生图/Flux2韩国小姐姐8步加速文生图（Lora版）_2006072352236376065.json、图片生成/文生图/flux2-dev-fp8-mixed 基础文生图_2006245362121580545.json、图片生成/文生图/【ComfyUI】三图精准编辑工作流｜结构+材质+物件分离替换+全注释_2061365487593943042.json、图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 6/7 个有
- `LoadImage` —— 4/7 个有
- `VAEEncode` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
