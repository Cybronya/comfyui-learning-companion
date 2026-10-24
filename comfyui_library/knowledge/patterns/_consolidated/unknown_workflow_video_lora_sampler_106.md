---
name: unknown_workflow_video_lora_sampler_106
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.801
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 文生视频加速KJ版+提示词选取_1951130910374699010.json, 视频生成/文生视频/Wan2.2 文生视频加速KJ版+运镜_1950408991886196738.json, 视频生成/文生视频/Wan2.2 文生视频加速KJ版_1950100642577694721.json, 视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json, 视频生成/文生视频/Wan2.2+Skyreels 5分镜提示词扩写文生无限长视频V1_1957481859263426562.json, 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1(贞贞版2000步)_1951167781284851713.json, 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V4(高质量横屏720P贞贞版)_1951179698393034754.json, 视频生成/文生视频/Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V4(高质量竖屏720P贞贞版)_1953444312275144706.json, 视频生成/文生视频/t2vV3_1956721780875300866.json, 视频生成/文生视频/wan2.2palingenesis智能提示词文生视频横屏版（包含自训练脸模lora保持角色一致性）_1973017295171751938.json, 视频生成/文生视频/wan2.2智能提示词文生视频竖屏版直出2k（包含自训练脸模lora保持角色一致性）_1968733813188829186.json, 视频生成/文生视频/✅Wan2.2-Lightx-文生视频-KJ版-720p_1950738636969021442.json, 视频生成/文生视频/（1+3四步版本）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972112233536876545.json, 视频生成/文生视频/（KJ版2+2极速）Wan2.2自动镜头新版lightning0928文生视频V3_1972282645650534402.json, 视频生成/文生视频/（电影质感版）Wan2.2+提示词工具+无API视频扩写3分镜文生视频版V5_1972106036679208961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 文生视频加速KJ版+提示词选取_1951130910374699010.json、视频生成/文生视频/Wan2.2 文生视频加速KJ版+运镜_1950408991886196738.json、视频生成/文生视频/Wan2.2 文生视频加速KJ版_1950100642577694721.json、视频生成/文生视频/Wan2.2 自动手动文生视频（UnifiedReward+VBVR逻辑增强）-二次元赛琳娜版_2029097055917969409.json、视频生成/文生视频/Wan2.2+Skyreels 5分镜提示词扩写文生无限长视频V1_1957481859263426562.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 15 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 14/15 个有
- `ShowText|pysssss` —— 13/15 个有
- `INTConstant` —— 12/15 个有
- `JWStringConcat` —— 12/15 个有
- `RH_LLMAPI_NODE` —— 12/15 个有
- `Wan22PromptSelector` —— 12/15 个有
- `WanVideoTorchCompileSettings` —— 12/15 个有
- `easy showAnything` —— 12/15 个有
- `JWInteger` —— 11/15 个有
- `TextConcat` —— 11/15 个有
- `ImageFromBatch+` —— 3/15 个有
- `Bjornulf_ShowInt` —— 2/15 个有
- `SimpleMath+` —— 2/15 个有
- `CR Text` —— 1/15 个有
- `GetNode` —— 1/15 个有
- `Int` —— 1/15 个有
- `JWFloat` —— 1/15 个有
- `KepStringLiteral` —— 1/15 个有
- `SetNode` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `easy seed` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
