---
name: unknown_workflow_video_sampler_clip_34
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.810357
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/4步首尾帧+自动提示词（短剧专用）_2000837178416656386.json, 视频生成/图生视频/8步首帧+自动提示词（短剧专用）_2000842508747800577.json, 视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json, 视频生成/图生视频/Wan2.2 14B 首尾帧_1989350434903085058.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json, 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json, 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1961778127099904002.json, 视频生成/图生视频/Wan2.2官方首尾帧优化版_1953457819821506562.json, 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频--智能扩写提示词版_1978821829475340289.json, 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json, 视频生成/图生视频/创意首尾帧视频制作 WAN2.2-LightX2V-I2V_1981037704194441217.json, 视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json, 视频生成/图生视频/首尾震·2张照片丝滑变视频_2010988628385730561.json, 视频生成/图生视频/高动态-图生视频-WAN2.2-LightX2V-I2V_1981728832514334722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/4步首尾帧+自动提示词（短剧专用）_2000837178416656386.json、视频生成/图生视频/8步首帧+自动提示词（短剧专用）_2000842508747800577.json、视频生成/图生视频/Wan2.2 14B 首尾帧_1968955228710133762.json、视频生成/图生视频/Wan2.2 14B 首尾帧_1989350434903085058.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/14 个有
- `RH_LLMAPI_NODE` —— 12/14 个有
- `PathchSageAttentionKJ` —— 11/14 个有
- `JWInteger` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/14 个有
- `CR Text` —— 9/14 个有
- `GetNode` —— 9/14 个有
- `ImpactSwitch` —— 9/14 个有
- `MathExpression|pysssss` —— 9/14 个有
- `SetNode` —— 9/14 个有
- `easy showAnything` —— 9/14 个有
- `LayerUtility: PurgeVRAM V2` —— 8/14 个有
- `WanFirstLastFrameToVideo` —— 7/14 个有
- `WanImageToVideo` —— 7/14 个有
- `CLIPVisionEncode` —— 6/14 个有
- `CLIPVisionLoader` —— 6/14 个有
- `ShowText|pysssss` —— 5/14 个有
- `wanBlockSwap` —— 5/14 个有
- `ImageConcanate` —— 4/14 个有
- `ImageResizeKJ` —— 4/14 个有
- `ModelPatchTorchSettings` —— 4/14 个有
- `SaveImage` —— 2/14 个有
- `Text Concatenate` —— 2/14 个有
- `Wan22PromptSelector` —— 2/14 个有
- `easy imageConcat` —— 2/14 个有
- `GetImageSizeAndCount` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `Primitive integer [Crystools]` —— 1/14 个有
- `RH_Nano_Banana_Image2Image` —— 1/14 个有
- `RIFE VFI` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有
- `WanVideoNAG` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 14 | 76% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | euler | - | 14 | 71% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，14 个样本
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，14 个样本，一致性 71%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
