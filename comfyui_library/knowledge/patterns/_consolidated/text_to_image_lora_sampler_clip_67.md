---
name: text_to_image_lora_sampler_clip_67
type: Text To Image
frequency: 16
level: strong
coverage: 0.903813
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json, 图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json, 图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json, 图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json, 图片生成/图生图/Qwen image 2.1图像编辑通用版｜图生图指令改图｜听懂人话好上手_2102285690850598914.json, 图片生成/图生图/Qwen image 2.1图片编辑 局部修改指令式操作_2105111897447157762.json, 图片生成/图生图/Qwen image 2.1图片编辑一号版｜图生图轻量改图首选_2112880073996062721.json, 图片生成/图生图/Qwen image 2.1图片编辑多面手｜图片换背景其它处理全包｜图生图顺手_2102252322154962946.json, 图片生成/图生图/Qwen image 2.1图片编辑轻量版｜小改动不求人｜抠字改背景都行_2102650761531445250.json, 图片生成/图生图/Qwen image 2.1图片编辑，海报制作场景特效全能_2112335625205669889.json, 图片生成/图生图/Qwen image 2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2102210466104832001.json, 图片生成/图生图/Qwen image 2.1多图编辑人物面部加全身三视图角色表V2_2109341094629699586.json, 图片生成/图生图/Qwen image 2.1多图编辑｜图生图多参考融合｜改图精准不跑偏_2104827606054035458.json, 图片生成/图生图/qwen image2.1多图编辑 换装场景道具一键替换_2104284093109334017.json, 图片生成/图生图/qwen image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2102257321794695170.json, 图片生成/图生图/多图编辑qwen image2.1｜场景道具换装 图生图多图协同编辑_2104110886465130498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1自动换头术图像编辑工作流，人像写真图生图处理工具_2108454879172849665.json、图片生成/图生图/Qwen Image 2.1角色三视图BF16展开版，可选择保留背景图生图工具_2106504632108408834.json、图片生成/图生图/Qwen Image2.1图生图三套夏装｜多套服装一键试穿_2108077360229732354.json、图片生成/图生图/Qwen Image2.1自动换头术｜图像编辑换脸局部重绘利器_2108034758382018561.json、图片生成/图生图/Qwen image 2.1图像编辑通用版｜图生图指令改图｜听懂人话好上手_2102285690850598914.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 15/16 个有
- `ComfySwitchNode` —— 10/16 个有
- `TextGenerateLTX2Prompt` —— 10/16 个有
- `easy showAnything` —— 10/16 个有
- `BatchImagesNode` —— 9/16 个有
- `ResolutionSelector` —— 8/16 个有
- `SaveImageAdvanced` —— 8/16 个有
- `CR Text` —— 4/16 个有
- `ImageConcatMulti` —— 3/16 个有
- `JDCN_StringToList` —— 3/16 个有
- `PrimitiveStringMultiline` —— 3/16 个有
- `ImageCompare` —— 2/16 个有
- `PrimitiveBoolean` —— 2/16 个有
- `WujiCleaner` —— 2/16 个有
- `WujiUpscaler2` —— 2/16 个有
- `Image Compare (mtb)` —— 1/16 个有
- `easy int` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
