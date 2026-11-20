---
name: unknown_workflow_video_sampler_vae_125
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9565
common_nodes: [ImagePadKJ, ImageResizeKJ, Int, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/字节开源Phantom 14B-多图参考电商带货-产品介绍视频生成-StarAI_1927665720824610817.json, 视频生成/图生视频/phantom图生视频工作流_1917413592033853442.json, 视频生成/图生视频/双图Phantom视频版FX人物一致性_1934212623216898050.json, 视频生成/图生视频/字节开源Phantom-多图参考电商带货-产品介绍视频生成-StarAI_1914926063179264002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_125

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/字节开源Phantom 14B-多图参考电商带货-产品介绍视频生成-StarAI_1927665720824610817.json、视频生成/图生视频/phantom图生视频工作流_1917413592033853442.json、视频生成/图生视频/双图Phantom视频版FX人物一致性_1934212623216898050.json、视频生成/图生视频/字节开源Phantom-多图参考电商带货-产品介绍视频生成-StarAI_1914926063179264002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `FILM VFI` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `WanVideoVACEEncode` —— 1/4 个有
- `easy imageScaleDownToSize` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
