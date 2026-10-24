---
name: text_to_image_lora_sampler_clip_221
type: Text To Image
frequency: 8
level: strong
coverage: 0.7795
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json, 图片生成/反推提示词/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json, 图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json, 图片生成/图生图/Remove模型Qwen Image 2.1 PE姿势编辑工作流，人物类特效擦除图生图_2106895128467173377.json, 图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json, 图片生成/图生图/超级加速版Qwen Image 2.1 PE图像编辑工作流，图生图图像处理方案_2108287006626369538.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，人像写真海报制作文本到图像方案_2107215861605031937.json, 图片生成/文生图/Qwen Image 2.1 PE文生图工作流，高质量文本到图像生成方案_2106466665084055554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_221

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen2.1整合版工作流，加入常用LoRA美化界面文生图图生图方案_2106441085731037185.json、图片生成/反推提示词/qwen2.1小岚整合版｜文生图反推提示词图生图三合一全套_2106208856383778817.json、图片生成/图生图/Qwen image 2.1姿势参考编辑 人物姿态精准控制_2109070115789692929.json、图片生成/图生图/Remove模型Qwen Image 2.1 PE姿势编辑工作流，人物类特效擦除图生图_2106895128467173377.json、图片生成/图生图/稳定加速版Qwen Image 2.1 PE姿势编辑 人物姿态精准控制_2109389400659554306.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `ComfySwitchNode` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `LoadImage` —— 6/8 个有
- `QwenImage21Cache` —— 6/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `GetNode` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `Context (rgthree)` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `JoinStringMulti` —— 2/8 个有
- `JoinStrings` —— 2/8 个有
- `easy anythingIndexSwitch` —— 2/8 个有
- `easy boolean` —— 2/8 个有
- `easy float` —— 2/8 个有
- `easy ifElse` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
