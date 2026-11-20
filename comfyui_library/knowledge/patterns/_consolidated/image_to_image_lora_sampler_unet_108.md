---
name: image_to_image_lora_sampler_unet_108
type: Image To Image
frequency: 6
level: strong
coverage: 0.775167
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_2511_千问一键多图融合参考自动拼接工作流_2003800899795468290.json, 图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json, 图片生成/图生图/Qwen_Camera_Control_Pro_1990243371115573250.json, 图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json, 图片生成/图生图/人物白底四视图一键生成_自动拼接无损超清放大_1996916628501762049.json, 视频生成/图生视频/一键自动生成女装详情页工作流_一键扣图_自动放大衣服细节_自动摆人物pose_2003817085564272641.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_108

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen_2511_千问一键多图融合参考自动拼接工作流_2003800899795468290.json、图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json、图片生成/图生图/Qwen_Camera_Control_Pro_1990243371115573250.json、图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json、图片生成/图生图/人物白底四视图一键生成_自动拼接无损超清放大_1996916628501762049.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CameraControlPromptNode` —— 4/6 个有
- `ImageUpscaleWithModel` —— 4/6 个有
- `UpscaleModelLoader` —— 4/6 个有
- `GetImageSize+` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `ImageScale` —— 3/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `EG_TX_SFBLS` —— 1/6 个有
- `GetImage` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（30/6 个样本）：Steps较低可能导致细节不足
