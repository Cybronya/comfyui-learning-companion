---
name: unknown_workflow_video_sampler_clip_72
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.914889
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json, 视频生成/图生视频/KJ-Wan2.1-图生视频_1895074790560956417.json, 视频生成/图生视频/KJ纯净版_图生视频_480p_1919644489483223042.json, 视频生成/图生视频/WANI2V彩色烟雾视频制作器-彩烟特效ZYP原创_1907459006556999682.json, 视频生成/图生视频/WAN复杂动作防崩图生视频工作流_1895519547200307202.json, 视频生成/图生视频/Wan图生视频高精度FP32版480P模型V1_1894619685634355201.json, 视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894653329455362049.json, 视频生成/图生视频/Wan图生视频高质量BF16版720P模型V1_1894658014006390785.json, 视频生成/图生视频/Wan无限延长抽帧图生视频工作流_1894765811745816578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/5秒图生视频生成 - Wan2.1_1898064124872740866.json、视频生成/图生视频/KJ-Wan2.1-图生视频_1895074790560956417.json、视频生成/图生视频/KJ纯净版_图生视频_480p_1919644489483223042.json、视频生成/图生视频/WANI2V彩色烟雾视频制作器-彩烟特效ZYP原创_1907459006556999682.json、视频生成/图生视频/WAN复杂动作防崩图生视频工作流_1895519547200307202.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `Note Plus (mtb)` —— 4/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `Note _O` —— 2/9 个有
- `WanVideoEnhanceAVideo` —— 2/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `SaveLatent` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `WanVideoLoraSelect` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
