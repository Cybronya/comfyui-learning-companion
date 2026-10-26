---
name: text_to_image_lora_sampler_clip_366
type: Text To Image
frequency: 5
level: strong
coverage: 0.839
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/爆款视频反推V2提示词分析视频脚本反推 提示词反推工具_2109392539609554946.json, 图片生成/反推提示词/短视频爆款拆解娱乐版｜反推提示词学套路｜热门视频结构一眼看穿_2102652141067390977.json, 图片生成/反推提示词/短视频爆款视频拆解娱乐版反推提示词处理工具_2101724950100008962.json, 图片生成/反推提示词/视频反推人像主体替换｜反推提示词高质量工作流_2095608214250409985.json, 图片生成/图生图/⭐️ 图片裂变3.0_2087140271216750593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_366

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/爆款视频反推V2提示词分析视频脚本反推 提示词反推工具_2109392539609554946.json、图片生成/反推提示词/短视频爆款拆解娱乐版｜反推提示词学套路｜热门视频结构一眼看穿_2102652141067390977.json、图片生成/反推提示词/短视频爆款视频拆解娱乐版反推提示词处理工具_2101724950100008962.json、图片生成/反推提示词/视频反推人像主体替换｜反推提示词高质量工作流_2095608214250409985.json、图片生成/图生图/⭐️ 图片裂变3.0_2087140271216750593.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_Pro_Node`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 4/5 个有
- `easy saveText` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `CR Text Replace` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `Any To String (mtb)` —— 1/5 个有
- `AspectRatioSelect` —— 1/5 个有
- `GoohaiUniversalSlider` —— 1/5 个有
- `LayerSeparationSaveText` —— 1/5 个有
- `RH_Captioner_Pro` —— 1/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
