---
name: unknown_workflow_video_sampler_clip_50
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.827455
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json, 数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json, 视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配（lora版）_1982062028078620674.json, 视频生成/图生视频/Wan2.2 Remix V2图生视频版_1986648481861431297.json, 视频生成/图生视频/Wan2.2-Dasiwa 二次元动漫_1990436662905901058.json, 视频生成/图生视频/Wan2.2-remix+VQA 首尾帧_1988124359338389506.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2 Remix_1987522876448419841.json, 视频生成/图生视频/图生视频 高画质，高动态 高遵循度 Wan2.2_2025865580863037441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/文生视频+高动态++Smooth+Mix+Wan2.2_2051825137523142657.json、数字人/数字人/二维漫画风格 Wan2.2-Dasiwa_2005829347586048001.json、视频生成/图生视频/Remix-Wan2.2 首尾帧 高动态画质_1987535452620173313.json、视频生成/图生视频/WAN2.2-LightX2V-I2V 图生视频最强动态搭配_1982410881613078529.json、视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980829288985444354.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 10/11 个有
- `CLIPVisionLoader` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `RH_LLMAPI_NODE` —— 10/11 个有
- `easy showAnything` —— 10/11 个有
- `wanBlockSwap` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `WanImageToVideo` —— 9/11 个有
- `LayerUtility: PurgeVRAM V2` —— 7/11 个有
- `CR Text Input Switch (4 way)` —— 5/11 个有
- `Text Concatenate` —— 5/11 个有
- `Wan22PromptSelector` —— 5/11 个有
- `AILab_QwenVL` —— 4/11 个有
- `CombinationText` —— 4/11 个有
- `ImpactSwitch` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `ImageConcanate` —— 2/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `WanFirstLastFrameToVideo` —— 2/11 个有
- `easy textSwitch` —— 2/11 个有
- `CompressImages` —— 1/11 个有
- `ImageStitch` —— 1/11 个有
- `PDIMAGE_LongerSize` —— 1/11 个有
- `Qwen3_VQA_Plus` —— 1/11 个有
- `RunningHub Deepcleaner` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 11 | 91% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler_ancestral | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，11 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
