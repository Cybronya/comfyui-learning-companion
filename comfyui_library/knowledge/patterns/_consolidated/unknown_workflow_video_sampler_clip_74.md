---
name: unknown_workflow_video_sampler_clip_74
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.754333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json, 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1961778127099904002.json, 视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json, 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json, 视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json, 视频生成/图生视频/王中王首尾帧微型--吊打闭源【万物生长 2】_1980857970835804161.json, 视频生成/图生视频/王炸首尾帧--吊打闭源【万物生长 】_1980631743067803649.json, 视频生成/图生视频/王炸首尾帧--吊打闭源【万物生长 】_2013871524415016962.json, 视频生成/图生视频/首尾帧 Wan2.2-Remix 高动态，高画质_1987524619294978050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json、视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1961778127099904002.json、视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json、视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json、视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 6/9 个有
- `CLIPVisionLoader` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `WanFirstLastFrameToVideo` —— 6/9 个有
- `ImageConcanate` —— 5/9 个有
- `ImageResizeKJ` —— 5/9 个有
- `ImpactSwitch` —— 5/9 个有
- `LayerUtility: PurgeVRAM V2` —— 5/9 个有
- `ModelPatchTorchSettings` —— 5/9 个有
- `wanBlockSwap` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `RIFE VFI` —— 4/9 个有
- `SeedVR2BlockSwap` —— 4/9 个有
- `SeedVR2ExtraArgs` —— 4/9 个有
- `SeedVR2GGUF` —— 4/9 个有
- `easy textSwitch` —— 4/9 个有
- `RH_Nano_Banana_Image2Image` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `WanImageToVideo` —— 3/9 个有
- `PromptTemplateSelector` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `WanVideoNAG` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 9 | 88% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler_ancestral | - | 9 | 56% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，9 个样本，一致性 56%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
