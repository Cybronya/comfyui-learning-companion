---
name: image_to_image_lora_sampler_unet_11
type: Image To Image
frequency: 24
level: strong
coverage: 0.91525
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN-2511 ｜ 一致性｜多角度九宫格｜自定义角度_2021655546507567106.json, 图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版+全节点注释_2052231197274714113.json, 图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2009868534964297730.json, 图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2042118585144840193.json, 图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-预设版_2009865153323470849.json, 图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-预设版_2020733052619591682.json, 图片生成/图生图/Qwen Multiangle 多角度一致性分镜工作流_2011317131958296578.json, 图片生成/图生图/Qwen Multiangle 多角度一致性分镜工作流_2013097150955134978.json, 图片生成/图生图/Qwen Multiangle 多角度一致性分镜工作流_2085038097712111618.json, 图片生成/图生图/Qwen-Image-Edit-2511模型多角度摄像控制（96种机位选择）+直观便捷操作一键生成_2049404246746992642.json, 图片生成/图生图/Qwen2511多角度可视化控制_2010534612233097218.json, 图片生成/图生图/Qwen2511多角度可视化控制流_2009809050485133313.json, 图片生成/图生图/Qwen2511多角度可视化控制流_2011993469119631362.json, 图片生成/图生图/Qwen_Multiangle_多角度一致性分镜工作流_2085543629942255618.json, 图片生成/图生图/Qwen_Multiangle_多角度一致性分镜工作流_2085562380796383233.json, 图片生成/图生图/qwen2511多角度提示词控制_2059192086624296961.json, 图片生成/图生图/qwen多角度_2009920085019856897.json, 图片生成/图生图/产品多视角_2029792715122155522.json, 图片生成/图生图/人物场景多角度分镜图生成（镜头角度可调整）_2054953876385746946.json, 图片生成/图生图/人设一致性多角度_2011272687615741953.json, 图片生成/图生图/亿薪AI多角度摄像控制（96种机位选择）+直观便捷操作_2013894548686114817.json, 图片生成/图生图/单角度摄像控制（背面专属版）+直观便捷操作_2064296017763332098.json, 图片生成/图生图/多角度2511一致性分镜_2069622645976559618.json, 图片生成/图生图/多角度多机位拍摄模特人物+自由变更机位便捷操作_2066874522317447170.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/QWEN-2511 ｜ 一致性｜多角度九宫格｜自定义角度_2021655546507567106.json、图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版+全节点注释_2052231197274714113.json、图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2009868534964297730.json、图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-自由控制版_2042118585144840193.json、图片生成/图生图/Qwen Multiangle Camera 2511多角度可视化控制-预设版_2009865153323470849.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KepStringList` —— 20/24 个有
- `easy showAnything` —— 20/24 个有
- `EmptySD3LatentImage` —— 17/24 个有
- `Int` —— 15/24 个有
- `Text Concatenate` —— 11/24 个有
- `easy string` —— 11/24 个有
- `PreviewAny` —— 3/24 个有
- `CR Text` —— 1/24 个有
- `Getter` —— 1/24 个有
- `ImageGetter` —— 1/24 个有
- `Kep_JoinListAny` —— 1/24 个有
- `Setter` —— 1/24 个有
- `TT_img_enc` —— 1/24 个有
- `Text Multiline` —— 1/24 个有
- `easy promptLine` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（24/24 个样本）：Steps较低可能导致细节不足
