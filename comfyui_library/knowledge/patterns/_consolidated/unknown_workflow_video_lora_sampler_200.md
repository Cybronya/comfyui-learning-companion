---
name: unknown_workflow_video_lora_sampler_200
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.878
common_nodes: [CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/AniWan超高动态图生视频_1946038864878202882.json, 视频生成/图生视频/1秒2帧！lightx2v最快16fps版高质量图生视频V1_1934999093192105986.json, 视频生成/图生视频/AccVid 加速Wan I2v图生视频V1_1929947388339765250.json, 视频生成/图生视频/AniWan专业动漫模型图生视频-更高运动幅度_1946761730153148417.json, 视频生成/图生视频/Wan2.1 PUSA+LightX2V 质量修复版_1946494882895523842.json, 视频生成/图生视频/Wan2.1 PUSA图生视频V1_1946072429141651458.json, 视频生成/图生视频/Wan2.1最高质量30秒长视频加速稳定版V1（图生视频）_1948954040869761026.json, 视频生成/图生视频/ani全能视频S专业动漫2.0模型版图生视频加速版v1_1944601523588354050.json, 视频生成/图生视频/ani全能视频S动漫图生视频加速版_1944648210231250946.json, 视频生成/图生视频/ani全能视频S动漫特化3.0模型版图生视频加速版v1_1961656258828943362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_200

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/AniWan超高动态图生视频_1946038864878202882.json、视频生成/图生视频/1秒2帧！lightx2v最快16fps版高质量图生视频V1_1934999093192105986.json、视频生成/图生视频/AccVid 加速Wan I2v图生视频V1_1929947388339765250.json、视频生成/图生视频/AniWan专业动漫模型图生视频-更高运动幅度_1946761730153148417.json、视频生成/图生视频/Wan2.1 PUSA+LightX2V 质量修复版_1946494882895523842.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `Text Multiline` —— 9/10 个有
- `WanVideoEnhanceAVideo` —— 9/10 个有
- `WanVideoExperimentalArgs` —— 8/10 个有
- `WanVideoSLG` —— 8/10 个有
- `WanVideoVRAMManagement` —— 8/10 个有
- `WanVideoFreeInitArgs` —— 6/10 个有
- `CR Text` —— 1/10 个有
- `EG_SZ_CGJS` —— 1/10 个有
- `Float` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `WanVideoEasyCache` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
