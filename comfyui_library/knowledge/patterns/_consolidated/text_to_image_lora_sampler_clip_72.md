---
name: text_to_image_lora_sampler_clip_72
type: Text To Image
frequency: 15
level: strong
coverage: 0.891333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json, 图片生成/图生图/Qwen Image 2.1图生图三套夏装工作流，图生图服装展示处理工具_2108281083262488578.json, 图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json, 图片生成/图生图/Qwen Image 2.1多参考图生图｜标准版稳定出图首选_2105137018840899585.json, 图片生成/图生图/Qwen Image 2.1多图编辑 多张输入精准改图_2105377023228203010.json, 图片生成/图生图/Qwen Image 2.1多图编辑Multi Image Editing工作流，角色设计图生图_2106164834009174018.json, 图片生成/图生图/Qwen Image 2.1多图编辑人物面部加全身三视图角色表，图生图工具_2105781931915964417.json, 图片生成/图生图/Qwen Image 2.1多图编辑图片编辑全节点注释处理工具_2102541742317850626.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，图生图高质量图像处理方案_2107899694994247682.json, 图片生成/图生图/Qwen Image 2.1多图编辑工作流，多图融合局部修改精准控制高效出图_2114433401469095937.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json, 图片生成/图生图/qwen image2.1多图编辑 换装场景道具一键替换_2104284093109334017.json, 图片生成/图生图/qwen image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2102257321794695170.json, 图片生成/图生图/千问Qwen Image 2.1多图编辑｜一次处理多张素材图_2103029100855255041.json, 图片生成/图生图/多图编辑qwen image2.1｜场景道具换装 图生图多图协同编辑_2104110886465130498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json、图片生成/图生图/Qwen Image 2.1图生图三套夏装工作流，图生图服装展示处理工具_2108281083262488578.json、图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json、图片生成/图生图/Qwen Image 2.1多参考图生图｜标准版稳定出图首选_2105137018840899585.json、图片生成/图生图/Qwen Image 2.1多图编辑 多张输入精准改图_2105377023228203010.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 14/15 个有
- `QwenImage21Cache` —— 13/15 个有
- `BatchImagesNode` —— 11/15 个有
- `TextGenerateLTX2Prompt` —— 11/15 个有
- `ResolutionSelector` —— 9/15 个有
- `ComfySwitchNode` —— 8/15 个有
- `CR Text` —— 7/15 个有
- `SaveImageAdvanced` —— 5/15 个有
- `easy showAnything` —— 5/15 个有
- `JDCN_StringToList` —— 4/15 个有
- `easy imageConcat` —— 2/15 个有
- `Anything Everywhere3` —— 1/15 个有
- `CR Prompt Text` —— 1/15 个有
- `EmptySD3LatentImage` —— 1/15 个有
- `RebelsKrea2OutpaintCanvas` —— 1/15 个有
- `RebelsKrea2OutpaintComposite` —— 1/15 个有
- `RebelsKrea2OutpaintEncode` —— 1/15 个有
- `RebelsKrea2OutpaintModelPatch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
