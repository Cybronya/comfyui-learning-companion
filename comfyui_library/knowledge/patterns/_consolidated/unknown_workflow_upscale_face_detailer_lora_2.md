---
name: unknown_workflow_upscale_face_detailer_lora_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8295
common_nodes: [CLIPLoader, CLIPTextEncode, CR Seed, CR Text, CR Text Concatenate, DetailerForEach, FaceDetailer, Fast Groups Bypasser (rgthree), ImageScaleBy, ImageUpscaleWithModel, ImpactMakeTileSEGS, ImpactSEGSLabelAssign, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, MediaPipeFaceMeshDetectorProvider //Inspire, PixaromaLabel, PreviewImage, RHHiddenNodes, ResolutionMaster, SAMLoader, SEGSPreview, SaveImage, ShowText|pysssss, StringListToString, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, WildcardPromptFromString, easy float, easy seed]
problems: []
missing: []
members: [图片生成/文生图/AINIMA 动漫专属模型 AI智能体自动书写提示词工作流  进阶修脸高清放大工作流_2071943296942952450.json, 图片生成/文生图/ANIMA - AI智能体扩写批量角色生成工作流_2071946894737231874.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/AINIMA 动漫专属模型 AI智能体自动书写提示词工作流  进阶修脸高清放大工作流_2071943296942952450.json、图片生成/文生图/ANIMA - AI智能体扩写批量角色生成工作流_2071946894737231874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Text`
- `CR Text Concatenate`
- `DetailerForEach`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactMakeTileSEGS`
- `ImpactSEGSLabelAssign`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `MediaPipeFaceMeshDetectorProvider //Inspire`
- `PixaromaLabel`
- `PreviewImage`
- `RHHiddenNodes`
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

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `GITSSchedulerFuncProvider` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `PreviewDetailerHookProvider` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SEGSUpscaler` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader_Optimized` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 22 | - | 2 | 18% |
| 采样算法 | 4.5 | - | 1 | 100% |
| 调度器 | er_sde | - | 2 | 50% |
| 重绘幅度 | 0.3 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 22，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- 调度器 最常用 er_sde，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
