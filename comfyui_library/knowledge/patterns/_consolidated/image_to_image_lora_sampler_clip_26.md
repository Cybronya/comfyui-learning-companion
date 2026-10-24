---
name: image_to_image_lora_sampler_clip_26
type: Image To Image
frequency: 9
level: strong
coverage: 0.863111
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物一键转换——亚克力立架_1946941574536421378.json, 图片生成/图生图/万物一键转换——绒毛玩偶_1946954844869681154.json, 图片生成/图生图/产品_人像精修_2071792524552921090.json, 图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json, 图片生成/图生图/产品融入背景v4 真实光影_1957824102613745665.json, 图片生成/图生图/人像精修+上妆-kontxet_1959201923981324289.json, 图片生成/图生图/人物一键卸妆与素颜还原_2060237604842467329.json, 图片生成/图生图/冰爷老杨简单溶图-提前PS（省钱版）_1966078677220061185.json, 图片生成/图生图/🐲电商产品完美溶图【透视矫正 光影融合】🐲_2001553801477779457.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/万物一键转换——亚克力立架_1946941574536421378.json、图片生成/图生图/万物一键转换——绒毛玩偶_1946954844869681154.json、图片生成/图生图/产品_人像精修_2071792524552921090.json、图片生成/图生图/产品精修工作流 一键出图细节文字保留_1956371792107634690.json、图片生成/图生图/产品融入背景v4 真实光影_1957824102613745665.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `FluxKontextImageScale` —— 5/9 个有
- `DetailTransfer` —— 3/9 个有
- `Fast Bypasser (rgthree)` —— 3/9 个有
- `ImpactInt` —— 3/9 个有
- `easy imageRemBg` —— 3/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `Text Concatenate` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `ChinesePrompt_Mix` —— 1/9 个有
- `FastCanvas` —— 1/9 个有
- `FastCanvasTool` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
