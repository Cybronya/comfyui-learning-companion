---
name: text_to_image_lora_sampler_clip_151
type: Text To Image
frequency: 11
level: strong
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-2.1文生图改版角色资产｜角色设计设定图专供_2112855940704849921.json, 图片生成/图生图/Qwen一键出人物三视图｜角色一致性拉满的图生图神器_2111264557317574658.json, 图片生成/图生图/qwen image 2.1角色表生成｜角色设定图批量产出参考模板_2113500742152708097.json, 图片生成/图生图/qwen-image-2.1多图编辑创意版｜其它图片处理加其他创意玩法｜改图随心_2102260297569488898.json, 图片生成/图生图/qwen-image-2.1官方图生图｜原版工作流稳定不翻车_2103090972849688577.json, 图片生成/图生图/qwen2.1图片编辑 局部修改指令式操作_2104703919430656001.json, 图片生成/图生图/qwen2.1图片编辑局部修改 指令式操作精准改图_2104975240785915906.json, 图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json, 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json, 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2.1文生图改版角色资产｜角色设计设定图专供_2112855940704849921.json、图片生成/图生图/Qwen一键出人物三视图｜角色一致性拉满的图生图神器_2111264557317574658.json、图片生成/图生图/qwen image 2.1角色表生成｜角色设定图批量产出参考模板_2113500742152708097.json、图片生成/图生图/qwen-image-2.1多图编辑创意版｜其它图片处理加其他创意玩法｜改图随心_2102260297569488898.json、图片生成/图生图/qwen-image-2.1官方图生图｜原版工作流稳定不翻车_2103090972849688577.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `QwenImage21Cache` —— 9/11 个有
- `ResolutionSelector` —— 8/11 个有
- `ComfySwitchNode` —— 7/11 个有
- `SaveImageAdvanced` —— 5/11 个有
- `Text` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `easy promptLine` —— 2/11 个有
- `1hew_AnySwitchSelect` —— 1/11 个有
- `CR Prompt List` —— 1/11 个有
- `CR Prompt Text` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
