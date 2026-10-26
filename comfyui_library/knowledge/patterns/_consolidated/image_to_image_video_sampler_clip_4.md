---
name: image_to_image_video_sampler_clip_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.920333
common_nodes: [Any To Any, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, Float, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_1998250117671059458.json, 图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_2003338801550327809.json, 图片生成/图生图/（自用）成人摄影Z-image + Qwen3自动洗图2K版_1993954685472227329.json]
source: knowledge_consolidation
---

# image_to_image_video_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_1998250117671059458.json、图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_2003338801550327809.json、图片生成/图生图/（自用）成人摄影Z-image + Qwen3自动洗图2K版_1993954685472227329.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `Any To Any`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `Float`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `DuckHideNode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `TT_img_enc` —— 1/3 个有
- `TT_img_enc_v2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | ddim_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
