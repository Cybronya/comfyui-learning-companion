---
name: image_to_image_sampler_clip_unet_134
type: Image To Image
frequency: 5
level: strong
coverage: 0.9262
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext提示词助手模板_1939535808275857410.json, 图片生成/文生图/根据提示词修改图片_2000153948931715074.json, 平台全量/kontext-图片一键消除水印_1947684695866781697.json, 平台全量/kontext-图片全自动消除水印 无需涂抹_2013621046095646722.json, 平台全量/kontext拥抱融合_1948683669910237185.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Kontext提示词助手模板_1939535808275857410.json、图片生成/文生图/根据提示词修改图片_2000153948931715074.json、平台全量/kontext-图片一键消除水印_1947684695866781697.json、平台全量/kontext-图片全自动消除水印 无需涂抹_2013621046095646722.json、平台全量/kontext拥抱融合_1948683669910237185.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/5 个有
- `Bjornulf_ShowStringText` —— 1/5 个有
- `GLM_Translation_Text` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LoadImageOutput` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 5 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，5 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
