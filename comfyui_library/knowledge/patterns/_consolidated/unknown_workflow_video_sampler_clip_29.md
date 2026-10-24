---
name: unknown_workflow_video_sampler_clip_29
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.812933
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json, 视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json, 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json, 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1961778127099904002.json, 视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json, 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json, 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json, 视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json, 视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json, 视频生成/图生视频/首尾震·2张照片丝滑变视频_2010988628385730561.json, 视频生成/图生视频/高动态-图生视频-WAN2.2-LightX2V-I2V_1981728832514334722.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧_1980878054304206850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json、视频生成/图生视频/Wan2.2_14B_图生视频 (4步加速)_1955097122862350338.json、视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速)_1966753554679705601.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2017158021029306369.json、视频生成/图生视频/Wan2.2_图生视频_4步极速版_ComfyUI官方流_2044039756232790017.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/15 个有
- `LoraLoaderModelOnly` —— 12/15 个有
- `PathchSageAttentionKJ` —— 11/15 个有
- `CR Text` —— 10/15 个有
- `GetNode` —— 10/15 个有
- `ImpactSwitch` —— 10/15 个有
- `JWInteger` —— 10/15 个有
- `MathExpression|pysssss` —— 10/15 个有
- `RH_LLMAPI_NODE` —— 10/15 个有
- `SetNode` —— 10/15 个有
- `WanImageToVideo` —— 10/15 个有
- `easy showAnything` —— 10/15 个有
- `CLIPVisionEncode` —— 7/15 个有
- `CLIPVisionLoader` —— 7/15 个有
- `LayerUtility: PurgeVRAM V2` —— 6/15 个有
- `wanBlockSwap` —— 6/15 个有
- `ImageConcanate` —— 5/15 个有
- `ImageResizeKJ` —— 5/15 个有
- `ModelPatchTorchSettings` —— 5/15 个有
- `WanFirstLastFrameToVideo` —— 5/15 个有
- `SaveImage` —— 2/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `Text Concatenate` —— 2/15 个有
- `Wan22PromptSelector` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `GetImageSizeAndCount` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `Primitive integer [Crystools]` —— 1/15 个有
- `RH_Nano_Banana_Image2Image` —— 1/15 个有
- `RIFE VFI` —— 1/15 个有
- `TT_img_enc` —— 1/15 个有
- `WanMotionScale` —— 1/15 个有
- `WanVideoNAG` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 53% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 15 | 80% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 73% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 53%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，15 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 73%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
