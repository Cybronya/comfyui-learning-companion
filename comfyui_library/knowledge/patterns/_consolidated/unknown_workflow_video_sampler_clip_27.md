---
name: unknown_workflow_video_sampler_clip_27
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.802625
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, GetNode, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, wanBlockSwap]
problems: []
missing: []
members: [图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配（lora版）_1982062028078620674.json, 视频生成/图生视频/Wan2.2 Remix V2图生视频版_1986648481861431297.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979541039348355074.json, 视频生成/图生视频/Wan2.2 Smooth Mix高动态图生视频V1_1979756399754383362.json, 视频生成/图生视频/Wan2.2+新版lightx2v加速-4步图生视频【官版】_1950101403698159617.json, 视频生成/图生视频/Wan2.2-Dasiwa 二次元动漫_1990436662905901058.json, 视频生成/图生视频/动漫短剧图生视频动态优化工作流（lora版+自动提示词）_1982328615742382081.json, 视频生成/图生视频/图生视频 Wan2.2 Remix 高画质高动态_1987454672774565889.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json, 视频生成/图生视频/图生视频工作流_2050780959615791106.json, 视频生成/图生视频/图生视频工作流_2054015321224302593.json, 视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json、视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json、视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json、视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配（lora版）_1982062028078620674.json、视频生成/图生视频/Wan2.2 Remix V2图生视频版_1986648481861431297.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 15/16 个有
- `CLIPVisionLoader` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `ModelPatchTorchSettings` —— 15/16 个有
- `RIFE VFI` —— 15/16 个有
- `easy showAnything` —— 15/16 个有
- `SeedVR2BlockSwap` —— 14/16 个有
- `SeedVR2ExtraArgs` —— 14/16 个有
- `SeedVR2GGUF` —— 14/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `Fast Groups Bypasser (rgthree)` —— 12/16 个有
- `Text Concatenate` —— 10/16 个有
- `Wan22PromptSelector` —— 10/16 个有
- `ImpactSwitch` —— 9/16 个有
- `ShowText|pysssss` —— 8/16 个有
- `LayerUtility: PurgeVRAM V2` —— 7/16 个有
- `CR Text Input Switch (4 way)` —— 6/16 个有
- `AILab_QwenVL` —— 5/16 个有
- `CombinationText` —— 5/16 个有
- `easy cleanGpuUsed` —— 5/16 个有
- `ImageConcanate` —— 3/16 个有
- `Text Multiline` —— 3/16 个有
- `VHS_LoadVideo` —— 2/16 个有
- `CompressImages` —— 1/16 个有
- `GetImageSizeAndCount` —— 1/16 个有
- `ImageStitch` —— 1/16 个有
- `PDIMAGE_LongerSize` —— 1/16 个有
- `RunningHub Deepcleaner` —— 1/16 个有
- `easy textSwitch` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 16 | 75% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 16 | 88% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler_ancestral | - | 16 | 94% |
| 重绘幅度 | simple | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，16 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，16 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，16 个样本，一致性 94%
- 重绘幅度 最常用 simple，16 个样本，一致性 100%
