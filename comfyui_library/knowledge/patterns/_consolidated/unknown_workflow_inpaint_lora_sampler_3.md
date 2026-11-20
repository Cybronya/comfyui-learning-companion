---
name: unknown_workflow_inpaint_lora_sampler_3
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.861231
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, ImageCrop, InpaintModelConditioning, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, SaveImage, SolidMask, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy imageScaleDownToSize, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/ICEdit 人物图像编辑_1920459393798701058.json, 图片生成/图生图/ICEdit-MoE 人物一致性换装_1918978007225008130.json, 图片生成/图生图/Prompt 修图｜IC-Edit 图像风格化_1920797981845422082.json, 图片生成/图生图/Prompt修图｜IC-EdIT 人物换服装_1920796011718184962.json, 图片生成/图生图/【relight】秒级ICEdit-MoE超强人物一致性图像编辑_1918660687436906498.json, 图片生成/图生图/【一键玩转ICEdit-MoE】人物简易换装_1921009794025721857.json, 图片生成/图生图/【媲美全能图片G4o】ICEdit-MoE图像编辑｜人物一致性编辑_1918948791171616769.json, 图片生成/图生图/【最新开源】ICEdit-MoE超强人物一致性图像编辑_1918663248131067906.json, 图片生成/图生图/人物一致性指令控制变化_1918897515356426241.json, 图片生成/图生图/啊癫 ICEdit图像编辑超越全能图片G4O_1921928761250365442.json, 图片生成/图生图/对标4O图片编辑ICEdit_1920513716566032385.json, 图片生成/图生图/换发型 + 人物一致性｜IC-Edit图像编辑_1920797233758015490.json, 图片生成/文生图/秒级ICEdit超强人物一致性图像编辑_1918129785032081409.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/ICEdit 人物图像编辑_1920459393798701058.json、图片生成/图生图/ICEdit-MoE 人物一致性换装_1918978007225008130.json、图片生成/图生图/Prompt 修图｜IC-Edit 图像风格化_1920797981845422082.json、图片生成/图生图/Prompt修图｜IC-EdIT 人物换服装_1920796011718184962.json、图片生成/图生图/【relight】秒级ICEdit-MoE超强人物一致性图像编辑_1918660687436906498.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SolidMask`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageScaleDownToSize`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleTiled` —— 11/13 个有
- `MaskPreview+` —— 11/13 个有
- `ShowText` —— 11/13 个有
- `easy seed` —— 11/13 个有
- `CR Upscale Image` —— 9/13 个有
- `Text Concatenate` —— 9/13 个有
- `ReplaceText` —— 4/13 个有
- `Float` —— 2/13 个有
- `PMRF` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `UpscaleImageByUsingModel` —— 2/13 个有
- `UpscaleModelLoader` —— 2/13 个有
- `LayerMask: MaskPreview` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 85% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 13 | 100% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 100% |
| 重绘幅度 | beta | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 85%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，13 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 100%
- 重绘幅度 最常用 beta，13 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
