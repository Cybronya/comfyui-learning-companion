---
name: text_to_image_upscale_face_detailer_lora_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.859
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, CR Text, CR Text Concatenate, DetailerForEach, EmptyLatentImage, FaceDetailer, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, ImpactMakeTileSEGS, ImpactSEGSLabelAssign, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, MediaPipeFaceMeshDetectorProvider //Inspire, PixaromaLabel, PreviewImage, ResolutionMaster, SAMLoader, SEGSPreview, SaveImage, ShowText|pysssss, StringListToString, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, WildcardPromptFromString, easy float, easy seed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json, 图片生成/文生图/Anima 原生文生图 _图生图 _ 双采进阶工作流_2071937526302068738.json]
source: knowledge_consolidation
---

# text_to_image_upscale_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima  ControlNet-LLLite 形态参考 _ 局部修改工作流_2071937535030415362.json、图片生成/文生图/Anima 原生文生图 _图生图 _ 双采进阶工作流_2071937526302068738.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Text`
- `CR Text Concatenate`
- `DetailerForEach`
- `EmptyLatentImage`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactMakeTileSEGS`
- `ImpactSEGSLabelAssign`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `MediaPipeFaceMeshDetectorProvider //Inspire`
- `PixaromaLabel`
- `PreviewImage`
- `ResolutionMaster`
- `SAMLoader`
- `SEGSPreview`
- `SaveImage`
- `ShowText|pysssss`
- `StringListToString`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `WildcardPromptFromString`
- `easy float`
- `easy seed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `AnimaLLLiteApply` —— 1/2 个有
- `CR Image Input Switch` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `Int` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 22 | - | 2 | 18% |
| 采样算法 | 4.5 | - | 1 | 100% |
| 调度器 | er_sde | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- 调度器 最常用 er_sde，2 个样本，一致性 50%
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
