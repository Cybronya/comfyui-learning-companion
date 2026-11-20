---
name: image_to_image_upscale_lora_sampler_23
type: Image To Image
frequency: 6
level: moderate
coverage: 0.7315
common_nodes: [Anything Everywhere3, CLIPLoader, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImpactInt, ImpactMinMax, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ProcessString, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4月Qwen-Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+4K高清放大-V6_2043317500800143361.json, 图片生成/图生图/Qwen-Edit251影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_2018976945718956033.json, 图片生成/图生图/Qwen-edit -2511 人物多角度 秒变多角度时尚大片_2006551514181017602.json, 图片生成/图生图/开源版超强Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_1995778793837047810.json, 图片生成/图生图/超强Qwen-Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_2006552060581384193.json, 图片生成/图生图/迄今超强万物（360度无死角）换角度Qwen image-edit2511版（稳）影视级别万物角色可视化角度编辑+可选4K高清放大-V2_1914961153469153281.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/4月Qwen-Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+4K高清放大-V6_2043317500800143361.json、图片生成/图生图/Qwen-Edit251影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_2018976945718956033.json、图片生成/图生图/Qwen-edit -2511 人物多角度 秒变多角度时尚大片_2006551514181017602.json、图片生成/图生图/开源版超强Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_1995778793837047810.json、图片生成/图生图/超强Qwen-Edit2511言出法随影视级别万物角色多角度切换自动分镜控制+可选4K高清放大-V3_2006552060581384193.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `ImpactMinMax`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ProcessString`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/6 个有
- `ShellAgentPluginOutputText` —— 5/6 个有
- `CFGNorm` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `SeedVR2BlockSwap` —— 3/6 个有
- `SeedVR2ExtraArgs` —— 3/6 个有
- `SeedVR2GGUF` —— 3/6 个有
- `CLIPTextEncode` —— 2/6 个有
- `ImageListToImageBatch` —— 2/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `TTP_Image_Assy` —— 2/6 个有
- `TTP_Image_Tile_Batch` —— 2/6 个有
- `TTP_Tile_image_size` —— 2/6 个有
- `VAEDecodeTiled` —— 2/6 个有
- `easy imageBatchToImageList` —— 2/6 个有
- `Qwen3_VQA_Plus` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `easy convertAnything` —— 1/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 6 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.15 - 1 | 6 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，6 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，6 个样本，取值分散，一致性仅 44%
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
