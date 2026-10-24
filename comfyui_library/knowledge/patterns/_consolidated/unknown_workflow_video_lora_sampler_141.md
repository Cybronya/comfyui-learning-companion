---
name: unknown_workflow_video_lora_sampler_141
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.98875
common_nodes: [Int, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1图生视频快速流myshell版本_1952757197195382785.json, 视频生成/图生视频/wan视频图生视频_1909948084502364162.json, 视频生成/图生视频/【Wan2.1】泼水变装+换装_1931328744601137153.json, 视频生成/图生视频/出来吧雷电法王_1934787989723914241.json, 视频生成/图生视频/动物跳海草舞_1938411003644153857.json, 视频生成/图生视频/变身美人鱼_1931540318901219330.json, 视频生成/图生视频/可灵同款特效泼水变装_1929806483200884737.json, 视频生成/图生视频/可灵同款特效泼水变装_2042132156083871746.json, 视频生成/图生视频/可灵同款特效泼水变装_2049016895038300162.json, 视频生成/图生视频/水底游泳拉布布_1934069436511117313.json, 视频生成/图生视频/特效泼水变装_1940599811882250242.json, 视频生成/图生视频/百变女郎N版_1940634031115628545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_141

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/WAN2.1图生视频快速流myshell版本_1952757197195382785.json、视频生成/图生视频/wan视频图生视频_1909948084502364162.json、视频生成/图生视频/【Wan2.1】泼水变装+换装_1931328744601137153.json、视频生成/图生视频/出来吧雷电法王_1934787989723914241.json、视频生成/图生视频/动物跳海草舞_1938411003644153857.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `TextInput_` —— 11/12 个有
- `ImageUpscaleWithModel` —— 10/12 个有
- `Upscale Model Loader` —— 10/12 个有
- `CR Text Concatenate` —— 7/12 个有
- `LoadAudio` —— 4/12 个有
- `SaveLatent` —— 2/12 个有
- `WanVideoTeaCache` —— 2/12 个有
- `ImageSizeAndBatchSize` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `ShellAgentPluginInputImage` —— 1/12 个有
- `ShellAgentPluginSaveVideoVHS` —— 1/12 个有
- `String Replace (mtb)` —— 1/12 个有
- `WanVideoVACEModelSelect` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
