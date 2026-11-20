---
name: unknown_workflow_inpaint_upscale_lora_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9168
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, Image Comparer (rgthree), ImageCrop, ImageUpscaleWithModel, InpaintModelConditioning, LoadImage, LoraLoaderModelOnly, MaskPreview+, SaveImage, SolidMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/ICEdit_指令图像编辑_1900163809556819969.json, 图片生成/图生图/prompt 修图 ｜ICEdit_指令图像编辑_1919929557040959489.json, 图片生成/图生图/全能图片G-4o同款 ICEdit-MoE极速超级人物一致性图生图_1918528928758038530.json, 图片生成/图生图/用嘴改图ICEdit-MoE完爆全能图片G-4o_1924448862227132417.json, 图片生成/图生图/🤖新ICEdit-MoE极速超级人物一致性图生图，完爆全能图片G-4o_1918518651564265474.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ICEdit_指令图像编辑_1900163809556819969.json、图片生成/图生图/prompt 修图 ｜ICEdit_指令图像编辑_1919929557040959489.json、图片生成/图生图/全能图片G-4o同款 ICEdit-MoE极速超级人物一致性图生图_1918528928758038530.json、图片生成/图生图/用嘴改图ICEdit-MoE完爆全能图片G-4o_1924448862227132417.json、图片生成/图生图/🤖新ICEdit-MoE极速超级人物一致性图生图，完爆全能图片G-4o_1918518651564265474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImageCrop`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `Text Concatenate` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `easy imageScaleDownToSize` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `ImageResize+` —— 2/5 个有
- `KSampler` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `GoogleTranslateTextNode` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 20 | 1 - 20 | 5 | 25% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | beta | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 20，观测区间 1 - 20，5 个样本，取值分散，一致性仅 25%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 beta，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
