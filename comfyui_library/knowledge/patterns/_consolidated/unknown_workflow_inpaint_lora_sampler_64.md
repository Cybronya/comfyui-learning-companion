---
name: unknown_workflow_inpaint_lora_sampler_64
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.75
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, Display Int (rgthree), DualCLIPLoader, FluxGuidance, GetImageSize+, ImageConcanate, ImageCrop+, InpaintModelConditioning, InvertMask, Joy_caption_two, Joy_caption_two_load, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, PreviewImage, SaveImage, Segment, ShowText|pysssss, StyleModelApply, StyleModelLoader, TeaCache, Text Find and Replace, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/把老婆放到沙发上-Ace Plus+Fill+Redux稳定添加改变V1_1899714855912521730.json, 平台全量/上山下海入洞穴REDUX+FILL+ACE人物场景融合_1906711400054501378.json, 平台全量/把小火车开进现实_1904885058338230273.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/把老婆放到沙发上-Ace Plus+Fill+Redux稳定添加改变V1_1899714855912521730.json、平台全量/上山下海入洞穴REDUX+FILL+ACE人物场景融合_1906711400054501378.json、平台全量/把小火车开进现实_1904885058338230273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `Display Int (rgthree)`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageConcanate`
- `ImageCrop+`
- `InpaintModelConditioning`
- `InvertMask`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `PreviewImage`
- `SaveImage`
- `Segment`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TeaCache`
- `Text Find and Replace`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 2/3 个有
- `CompileModel` —— 2/3 个有
- `RMBG` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `image_concat_mask(rh)` —— 2/3 个有
- `BiRefNet` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LayerUtility: ExtendCanvas` —— 1/3 个有
- `ReActorFaceSwap` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
