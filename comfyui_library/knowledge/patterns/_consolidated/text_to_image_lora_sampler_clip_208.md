---
name: text_to_image_lora_sampler_clip_208
type: Text To Image
frequency: 9
level: strong
coverage: 0.869111
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1透明背景抠图，PNG通道输出图生图专用工作流_2102867983600283649.json, 图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json, 图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json, 图片生成/图生图/Qwen image 2.1图片编辑多面手｜图片换背景其它处理全包｜图生图顺手_2102252322154962946.json, 图片生成/图生图/Qwen image 2.1图片编辑轻量版｜小改动不求人｜抠字改背景都行_2102650761531445250.json, 图片生成/图生图/Qwen image 2.1图片编辑，海报制作场景特效全能_2112335625205669889.json, 图片生成/图生图/Qwen image 2.1多图编辑｜图生图多参考融合｜改图精准不跑偏_2104827606054035458.json, 图片生成/文生图/千问QWEN image 2.1文生图加图生图整合流 二合一方案_2109763974085562370.json, 视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_208

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1透明背景抠图，PNG通道输出图生图专用工作流_2102867983600283649.json、图片生成/图生图/Qwen Image 2.1配件编辑实测｜换配饰改道具轻松搞定_2103083517977645057.json、图片生成/图生图/Qwen Image 2.1｜文生图图生图二合一整合流｜抠图也能一键搞定_2102568018860666881.json、图片生成/图生图/Qwen image 2.1图片编辑多面手｜图片换背景其它处理全包｜图生图顺手_2102252322154962946.json、图片生成/图生图/Qwen image 2.1图片编辑轻量版｜小改动不求人｜抠字改背景都行_2102650761531445250.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `easy showAnything` —— 7/9 个有
- `ImageConcatMulti` —— 5/9 个有
- `SaveImageAdvanced` —— 5/9 个有
- `TextGenerateLTX2Prompt` —— 4/9 个有
- `BatchImagesNode` —— 3/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `PlaySound|pysssss` —— 2/9 个有
- `TextCombinerTwo` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `easy int` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `Image Compare (mtb)` —— 1/9 个有
- `QwenImage21PromptEnhancerT8` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
