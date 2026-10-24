---
name: unknown_workflow_upscale_lora_sampler_37
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.92
common_nodes: [CLIPLoader, CR Prompt Text, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json, 图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json, 图片生成/图生图/qwen2.1移除水印_2110973181870821378.json, 图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json, 视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json、图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json、图片生成/图生图/qwen2.1移除水印_2110973181870821378.json、图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json、视频生成/文生视频/Qwen-Image-2.1｜商品_主体任意溶图｜40步质量 + Viggle加速双路线_2107775767450046466.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `FastCanvas` —— 2/5 个有
- `FastCanvasTool` —— 2/5 个有
- `FluxGuidance` —— 2/5 个有
- `ImageCropper` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SaveImageAdvanced` —— 2/5 个有
- `TTP_Expand_And_Mask` —— 2/5 个有
- `Image Rembg (Remove Background)` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 40 | 26 - 40 | 5 | 80% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 40，观测区间 26 - 40，5 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
