---
name: unknown_workflow_video_lora_sampler_144
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9815
common_nodes: [Int, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952757197195382785.json, 视频生成/图生视频/1909948084502364162.json, 视频生成/图生视频/1899035898183372801.json, 视频生成/图生视频/1934787989723914241.json, 视频生成/图生视频/1938411003644153857.json, 视频生成/图生视频/1931540318901219330.json, 视频生成/图生视频/1929806483200884737.json, 视频生成/图生视频/2042132156083871746.json, 视频生成/图生视频/2049016895038300162.json, 视频生成/图生视频/1934069436511117313.json, 视频生成/图生视频/1940599811882250242.json, 视频生成/图生视频/1940634031115628545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_144

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1952757197195382785.json、视频生成/图生视频/1909948084502364162.json、视频生成/图生视频/1899035898183372801.json、视频生成/图生视频/1934787989723914241.json、视频生成/图生视频/1938411003644153857.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `MathExpression|pysssss` —— 11/12 个有
- `ImageUpscaleWithModel` —— 10/12 个有
- `Upscale Model Loader` —— 10/12 个有
- `CR Text Concatenate` —— 7/12 个有
- `LoadAudio` —— 4/12 个有
- `SaveLatent` —— 2/12 个有
- `WanVideoTeaCache` —— 2/12 个有
- `RH_Captioner` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `ShellAgentPluginInputImage` —— 1/12 个有
- `ShellAgentPluginSaveVideoVHS` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `String Replace (mtb)` —— 1/12 个有
- `WanVideoVACEModelSelect` —— 1/12 个有
- `easy promptConcat` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
