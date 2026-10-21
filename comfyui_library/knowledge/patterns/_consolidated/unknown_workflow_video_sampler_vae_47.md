---
name: unknown_workflow_video_sampler_vae_47
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.974667
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json, 视频生成/图生视频/1896112344349474817.json, 视频生成/图生视频/1948656923534077953.json, 视频生成/图生视频/1898064124872740866.json, 视频生成/图生视频/1920649191725400066.json, 视频生成/图生视频/1946953105147211777.json, 视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json, 视频生成/图生视频/1940715917842214913.json, 视频生成/文生视频/1948656923534077953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/2025重磅更新WANX2.1模型，内含图生视频！文生视频，高清720p_1896112344349474817.json、视频生成/图生视频/1896112344349474817.json、视频生成/图生视频/1948656923534077953.json、视频生成/图生视频/1898064124872740866.json、视频生成/图生视频/1920649191725400066.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `LoadWanVideoClipTextEncoder` —— 6/9 个有
- `WanVideoImageClipEncode` —— 6/9 个有
- `WanVideoLoraSelect` —— 6/9 个有
- `WanVideoEmptyEmbeds` —— 5/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `WanVideoEncode` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `Note _O` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
