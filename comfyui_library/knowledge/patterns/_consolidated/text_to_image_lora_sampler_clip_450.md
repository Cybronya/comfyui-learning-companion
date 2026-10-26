---
name: text_to_image_lora_sampler_clip_450
type: Text To Image
frequency: 4
level: strong
coverage: 0.66975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RH_Nano_Banana2_Gemini31Flash, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键出角色三视图｜SD2.0与H3超强一致性服装饰品_2096279296728977410.json, 图片生成/图生图/人物换脸1.0.1版｜高质量图生图脸部替换生成_2095935921358204930.json, 图片生成/图生图/美女换装1.0.1版｜RH2服装替换图生图生成_2096334228534419457.json, 图片生成/图生图/详情页制作风格参考一键生成｜平面广告设计电商海报复刻，图生图套版即出_2100493449488330753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_450

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键出角色三视图｜SD2.0与H3超强一致性服装饰品_2096279296728977410.json、图片生成/图生图/人物换脸1.0.1版｜高质量图生图脸部替换生成_2095935921358204930.json、图片生成/图生图/美女换装1.0.1版｜RH2服装替换图生图生成_2096334228534419457.json、图片生成/图生图/详情页制作风格参考一键生成｜平面广告设计电商海报复刻，图生图套版即出_2100493449488330753.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `DF_Text_Box` —— 2/4 个有
- `RH_RhartImageG2ImageToImage` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `CR Text Replace` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
