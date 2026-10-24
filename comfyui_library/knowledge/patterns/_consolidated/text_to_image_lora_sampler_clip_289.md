---
name: text_to_image_lora_sampler_clip_289
type: Text To Image
frequency: 6
level: strong
coverage: 0.8095
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewAny, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json, 图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json, 图片生成/图生图/G-image2五图参考低价版｜图生图多图融合_2094497916810514434.json, 图片生成/图生图/低价版G-image2｜短剧广告设计摄影图生图生成_2094726703590498305.json, 图片生成/图生图/全能图片V2图生图官方版｜提示词优化稳定出图新手放心用_2106213567543472129.json, 图片生成/图生图/全能图片V2图生图官方稳定版提示词优化工作流，图生图处理方案_2106513907606188034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_289

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json、图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json、图片生成/图生图/G-image2五图参考低价版｜图生图多图融合_2094497916810514434.json、图片生成/图生图/低价版G-image2｜短剧广告设计摄影图生图生成_2094726703590498305.json、图片生成/图生图/全能图片V2图生图官方版｜提示词优化稳定出图新手放心用_2106213567543472129.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `RH_RhartImageG2ImageToImage` —— 4/6 个有
- `RHLLMChatNode` —— 3/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `RHSettingsNode` —— 2/6 个有
- `RH_RhartImageG2TextToImage` —— 2/6 个有
- `SaveText` —— 1/6 个有
- `easy saveText` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
