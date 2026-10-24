---
name: unknown_workflow_video_lora_sampler_276
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.989375
common_nodes: [CLIPVisionLoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/最强逼真版图生视频lightx2_1935209763875508226.json, 视频生成/图生视频/角色_物品360度旋转_1946542261884870657.json, 视频生成/图生视频/🦖AniWan 变成方块人_1945368042832371714.json, 视频生成/图生视频/🦖AniWan版首尾帧_1945027007760752641.json, 视频生成/图生视频/🦖AniWan版高质量高动态图生视频_1945016400298827777.json, 视频生成/图生视频/🦖极速展翅_1943493844422062081.json, 视频生成/图生视频/🦖极速展翅_1977981192005976065.json, 视频生成/图生视频/🦖极速版万物消散_1946134674865614850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_276

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/最强逼真版图生视频lightx2_1935209763875508226.json、视频生成/图生视频/角色_物品360度旋转_1946542261884870657.json、视频生成/图生视频/🦖AniWan 变成方块人_1945368042832371714.json、视频生成/图生视频/🦖AniWan版首尾帧_1945027007760752641.json、视频生成/图生视频/🦖AniWan版高质量高动态图生视频_1945016400298827777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoExperimentalArgs` —— 7/8 个有
- `WanVideoFreeInitArgs` —— 7/8 个有
- `WanVideoSLG` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 6/8 个有
- `ImageResize+` —— 4/8 个有
- `MathExpression|pysssss` —— 4/8 个有
- `WanVideoTeaCache` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `WanVideoVRAMManagement` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `WanVideoEasyCache` —— 1/8 个有
- `WanVideoLoraSelectMulti` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
