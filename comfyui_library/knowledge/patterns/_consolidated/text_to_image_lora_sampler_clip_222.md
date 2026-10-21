---
name: text_to_image_lora_sampler_clip_222
type: Text To Image
frequency: 5
level: weak
coverage: 0.8728
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy saveText]
members: [图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json, 图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json, 图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json, 图片生成/图生图/2102276173383421953.json, 图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_222

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json、图片生成/反推提示词/小说剧本转标准JSON预处理搭配全栈式短剧生成V4.2.1使用工具_2105783383883345922.json、图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json、图片生成/图生图/2102276173383421953.json、图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `solarL_SaveImagesToZip` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `easy saveText` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImpactMakeImageList` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/5 个有
- `SaveText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 5 | 0% |
| 高度 | 80 | 80 - 1920 | 5 | 0% |
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 63% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy saveText
