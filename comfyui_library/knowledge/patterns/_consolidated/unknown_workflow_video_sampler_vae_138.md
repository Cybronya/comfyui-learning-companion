---
name: unknown_workflow_video_sampler_vae_138
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95475
common_nodes: [JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1923636242792312834.json, 视频生成/图生视频/1924304259204960258.json, 视频生成/文生视频/1923351101066629121.json, 视频生成/文生视频/1922867883611930626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_138

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1923636242792312834.json、视频生成/图生视频/1924304259204960258.json、视频生成/文生视频/1923351101066629121.json、视频生成/文生视频/1922867883611930626.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `Bjornulf_ShowJson` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
