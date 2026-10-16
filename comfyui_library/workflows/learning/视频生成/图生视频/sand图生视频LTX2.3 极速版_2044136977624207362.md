---
key: 视频生成/图生视频/sand图生视频LTX2.3 极速版_2044136977624207362.json
name: sand图生视频LTX2.3 极速版_2044136977624207362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044136977624207362.json
hash: 2e07de319041cceb
coverage: 0.857143
learned_at: 2026-10-15 22:36:36
nodes: [EmptyImage, CLIPTextEncode, SaveVideo, CLIPTextEncode, PrimitiveInt, workflow>重要, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/sand图生视频LTX2.3 极速版_2044136977624207362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044136977624207362.json`

## 结构

**生成流程**：Condition → Process → Output → Other

**节点**（7 个）：
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `workflow>重要`
- `LoadImage`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`EmptyImage`、`CLIPTextEncode`、`SaveVideo`、`workflow>重要`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、SaveVideo、EmptyImage、workflow>重要、sd15-t2i-basic、sd15-t2i-lora、Int
